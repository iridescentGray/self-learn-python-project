import gitlab


class GitLabApi(object):
    def __init__(self, url: str, token: str):
        self.api = gitlab.Gitlab(url, token)

    def get_projects_id(self, id):
        # 根据id获取项目
        res = self.api.projects.get(id)
        return res.attributes

    def get_projects_search(self, name):
        # 模糊搜索项目
        projects = self.api.projects.list(search=name)
        projectslist = []
        for pro in projects:
            projectslist.append(pro.attributes)
        return projectslist

    def create_project(self, name):
        # 创建项目
        res = self.api.projects.create({"name": name})
        return res.attributes

    def get_project_brances(self, id):
        # 获取项目所有分支
        project = self.api.projects.get(id)
        brancheslist = []
        for branches in project.branches.list():
            brancheslist.append(branches.attributes)
        return brancheslist

    def get_project_brance_attribute(self, id, branch):
        # 　获取指定项目指定分支
        project = self.api.projects.get(id)
        res = project.branches.get(branch)
        return res.attributes

    def create_get_project_brance(self, id, branch):
        # 　创建分支
        project = self.api.projects.get(id)
        res = project.branches.create({"branch": branch, "ref": "master"})
        return res.attributes

    def delete_project_brance(self, id, branch):
        # 删除分支
        project = self.api.projects.get(id)
        project.branches.delete(branch)

    def get_project_tags(self, id):
        # 获取所有的tag
        project = self.api.projects.get(id)
        tags = project.tags.list()
        taglist = []
        for tag in tags:
            taglist.append(tag.attributes)
        return taglist

    def get_project_tag_name(self, id, name):
        # 获取指定的tag
        project = self.api.projects.get(id)
        tags = project.tags.get(name)
        return tags.attributes

    def create_project_tag(self, id, name, branch="master"):
        # 创建tag
        project = self.api.projects.get(id)
        tags = project.tags.create({"tag_name": name, "ref": branch})
        return tags.attributes

    def delete_project_tag(self, id, name):
        # 删除tag
        project = self.api.projects.get(id)
        project.tags.delete(name)

    def get_project_commits(self, id):
        # 获取所有的commit
        project = self.api.projects.get(id)
        commits = project.commits.list()
        commitslist = []
        for com in commits:
            commitslist.append(com.attributes)
        return commitslist

    def get_project_commit_info(self, id, short_id):
        # 获取指定的commit
        project = self.api.projects.get(id)
        commit = project.commits.get(short_id)
        return commit.attributes
